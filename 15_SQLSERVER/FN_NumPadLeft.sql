USE [WangExport]
GO
/****** Object:  UserDefinedFunction [dbo].[FN_NumPadLeft]    Script Date: 8/3/2020 12:33:38 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER FUNCTION [dbo].[FN_NumPadLeft] (@input bigint, @pad tinyint)
RETURNS VARCHAR(250)
AS BEGIN
    DECLARE @NumStr VARCHAR(250)

    SET @NumStr = LTRIM(@input)

    IF(@pad > LEN(@NumStr))
        SET @NumStr = REPLICATE('0', @Pad - LEN(@NumStr)) + @NumStr;

    RETURN @NumStr;
END


/*
examples 

SELECT [dbo].[FN_NumPadLeft] (123,5)  -> '00123'
SELECT [dbo].[FN_NumPadLeft] (11,2)  -> '11'

*/