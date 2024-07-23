USE [WangImport]
GO
/****** Object:  Trigger [dbo].[TR_NewBusiness]    Script Date: 8/3/2018 9:16:29 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =======================================================================================================================================
-- Author: Oren Bezalely
-- Create date: 08/01/18
-- Name: TR_TestTrigger
-- Description:	Executes SP_NewBusinessData <latestID> when an INSERT is done into [WangImport].[dbo].[PolicyPaymentPlanInfo] 
--              which is the last table populated in the event of New Business
-- =======================================================================================================================================

ALTER TRIGGER [dbo].[TR_NewBusiness]

ON [WangImport].[dbo].[PolicyPaymentPlanInfo] 

AFTER INSERT

AS

BEGIN
	declare @ds varchar(255)
	SET @ds = (CAST(CAST(GETDATE() as Datetime2 (3)) as varchar(150)))
	INSERT INTO WangExport.dbo.TmpOren VALUES (@ds)
	DECLARE @newID int
	SELECT TOP 1 @newID = ID FROM Policy ORDER BY ID DESC

	--WAITFOR DELAY '00:00:50';
	EXEC WangExport.dbo.SP_NewBusinessData @newID
END