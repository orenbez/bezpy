USE [WangExport]
GO
/****** Object:  StoredProcedure [dbo].[SP_QueryToCsv]    Script Date: 8/3/2018 12:00:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
/*
-- =======================================================================================================================================
-- Author: Oren Bezalely
-- Create date: 7/27/18
-- Description:	Writes an sql query as a formatted CSV string.  CURRRENTLY NOT IN USE
-- Sample Usage: 
			DECLARE @csv nvarchar(max)
			EXEC [dbo].[SP_QueryToCsv]  @query = 'Select top 3 INV_ACCOUNT_NUMBER, INV_SUFFIX from INVOICE', @csv = @csv OUTPUT
			PRINT @csv
-- Additional Notes: Any ORDER BY clause needs to be passed in the separate @orderBy parameter.
-- =======================================================================================================================================
*/

ALTER PROC [dbo].[SP_QueryToCsv] 
(
  @query   nvarchar(MAX),               --A query to turn into CSV format. It should not include an ORDER BY clause.
  @orderBy nvarchar(MAX) = NULL,        --An optional ORDER BY clause. It should contain the words 'ORDER BY'.
  @csv     nvarchar(MAX) = NULL OUTPUT  --The CSV output of the procedure.
)
AS
BEGIN   
  SET NOCOUNT ON;

  IF @orderBy IS NULL BEGIN
    SET @orderBy = '';
  END

  SET @orderBy = REPLACE(@orderBy, '''', '''''');  

  DECLARE @realQuery nvarchar(MAX) = '
    DECLARE @headerRow nvarchar(MAX);
    DECLARE @cols nvarchar(MAX);

    SELECT * INTO #dynSql FROM (' + @query + ') sub;    

    SELECT @cols = ISNULL(@cols + '' + '''','''' + '', '''') + ''''''"'''' + ISNULL(REPLACE(CAST(['' + name + ''] AS nvarchar(max)), ''''"'''', ''''""''''), '''''''') + ''''"''''''
    FROM tempdb.sys.columns 
    WHERE object_id = object_id(''tempdb..#dynSql'')
    ORDER BY column_id;        

    SET @cols = ''
      SET @csv = (SELECT '' + @cols + '' FROM #dynSql ' + @orderBy + ' FOR XML PATH(''''m_m''''));
      ''
    EXEC sys.sp_executesql @cols, N''@csv nvarchar(MAX) OUTPUT'', @csv=@csv OUTPUT    

    SELECT @headerRow = ISNULL(@headerRow + '','', '''') + ''"'' + REPLACE(name, ''"'', ''""'') + ''"''
    FROM tempdb.sys.columns 
    WHERE object_id = object_id(''tempdb..#dynSql'')
    ORDER BY column_id;

    SET @headerRow = @headerRow + CHAR(13) + CHAR(10);

    SET @csv = @headerRow + @csv;    
    ';

  EXEC sys.sp_executesql @realQuery, N'@csv nvarchar(MAX) OUTPUT', @csv=@csv OUTPUT
  SET @csv = REPLACE(REPLACE(@csv, '<m_m>', ''), '</m_m>', CHAR(13) + CHAR(10))
END




/*

Declare @x nvarchar(max)
SET @x = dbo.FN_Decode2UTF8('hello,goodbye,xxx,yyy')
EXEC SP_WriteToFile  @x, 'C:\AIT\NewPolicyData', 'tmp3.csv'


DECLARE @strbcpcmd NVARCHAR(max)
SET @strbcpcmd =  'bcp  "Select top 3 INV_ACCOUNT_NUMBER, INV_SUFFIX from INVOICE" queryout "C:\AIT\NewPolicyData\test.txt" -w -C OEM -t"$" -T -S'+@@servername    
EXEC master..xp_cmdshell @strbcpcmd
*/

