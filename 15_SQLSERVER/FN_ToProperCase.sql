USE [WangExport]
GO
/****** Object:  UserDefinedFunction [dbo].[FN_ToProperCase]    Script Date: 8/3/2020 12:34:17 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER FUNCTION [dbo].[FN_ToProperCase]( @name nvarchar(500) )
RETURNS nvarchar(500)
AS
BEGIN
declare @pos    int = 1
      , @pos2   int

if (@name <> '')--or @name = lower(@name) collate SQL_Latin1_General_CP1_CS_AS or @name = upper(@name) collate SQL_Latin1_General_CP1_CS_AS)
begin
    set @name = lower(rtrim(@name))
    while (1 = 1)
    begin
        set @name = stuff(@name, @pos, 1, upper(substring(@name, @pos, 1)))
        set @pos2 = patindex('%[- ''.)(]%', substring(@name, @pos, 500))
        set @pos += @pos2
        if (isnull(@pos2, 0) = 0 or @pos > len(@name))
            break
    end
end

return @name
END
