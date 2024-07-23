USE [WangExport]
GO
/****** Object:  UserDefinedFunction [dbo].[FN_MaxValue]    Script Date: 8/3/2020 12:32:16 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =======================================================================================================================================
-- Author: Oren Bezalely
-- Create date: 11/15/18
-- Modification date: 
--                    
-- Description:	Returns largest value
-- Usage:       SELECT dbo.FN_MaxValue(34.5,77.9)
-- =======================================================================================================================================


ALTER FUNCTION [dbo].[FN_MaxValue](@Flt1 Float, @Flt2 Float)
RETURNS Float
AS
BEGIN
	DECLARE @Max Float
	IF @Flt2 < @Flt1 
		SET @Max = @Flt1 
	ELSE 
		SET @Max = @Flt2 

RETURN @Max
END
