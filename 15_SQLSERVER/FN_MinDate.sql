USE [WangExport]
GO
/****** Object:  UserDefinedFunction [dbo].[FN_MinDate]    Script Date: 8/3/2020 12:32:50 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =======================================================================================================================================
-- Author: Oren Bezalely
-- Create date: 11/6/18
-- Modification date: 
--                    
-- Description:	Returns earliest date from pair of dates
-- Usage: SELECT dbo.FN_MinDate('1970-01-01','2038-01-09')
-- =======================================================================================================================================


ALTER FUNCTION [dbo].[FN_MinDate](@Date1 Date, @Date2 Date)
RETURNS Date
AS
BEGIN
	DECLARE @Mindate Date
	IF @Date1 < @Date2 
		SET @Mindate = @Date1 
	ELSE 
		SET @Mindate = @Date2 

RETURN @Mindate
END