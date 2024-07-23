USE [WangExport]
GO
/****** Object:  UserDefinedFunction [dbo].[FN_Decode2UTF8]    Script Date: 8/3/2020 12:31:17 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER FUNCTION [dbo].[FN_Decode2UTF8]
(
  @str nvarchar(max)
 )
RETURNS nvarchar(max)
AS
BEGIN 
    DECLARE @Position INT,
        @Base CHAR(16),
        @Code INT,
        @Pattern CHAR(21)

    SELECT @str = REPLACE(@str, '%c3', '')

    SELECT  @Base = '0123456789abcdef',
        @Pattern = '%[%][0-9a-f][0-9a-f]%',
        @Position = PATINDEX(@Pattern, @str)

    WHILE @Position > 0
        SELECT @Code = Cast(CONVERT(varbinary(4), '0x' + SUBSTRING(@str, @Position + 1, 2), 1) As int),
            @str = STUFF(@str, @Position, 3, NCHAR(@Code + 64)),
            @Position = PATINDEX(@Pattern, @str)

    RETURN REPLACE(@str, '+', ' ')

END