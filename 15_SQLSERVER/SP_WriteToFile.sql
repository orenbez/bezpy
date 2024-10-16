USE [WangExport]
GO
/****** Object:  StoredProcedure [dbo].[SP_WriteToFile]    Script Date: 8/3/2018 12:03:15 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =======================================================================================================================================
-- Author: Oren Bezalely
-- Create date: 7/27/18
-- Description:	Writes String to File on Server
-- Sample Usage: EXEC dbo.SP_WriteToFile 'string of data', 'C:\AIT\NewPolicyData', 'fileName.txt'
-- =======================================================================================================================================

ALTER PROCEDURE [dbo].[SP_WriteToFile]
 (
		@String nvarchar(max),
		@Path varchar(255),
		@Filename varchar(100)
)
AS
DECLARE  @objFileSystem int,
		 @objTextStream int,
		 @objErrorObject int,
		 @strErrorMessage varchar(1000),
	     @Command varchar(1000),
	     @hr int,
		 @fileAndPath varchar(80) 
		 SET @string = WangExport.dbo.FN_Decode2UTF8(@string)
set nocount on

select @strErrorMessage='opening the File System Object'
EXECUTE @hr = sp_OACreate  'Scripting.FileSystemObject' , @objFileSystem OUT

Select @FileAndPath=@path+'\'+@filename
if @HR=0 Select @objErrorObject=@objFileSystem , @strErrorMessage='Creating file "'+@FileAndPath+'"'
if @HR=0 execute @hr = sp_OAMethod   @objFileSystem   , 'CreateTextFile'
	, @objTextStream OUT, @FileAndPath,2,True

if @HR=0 Select @objErrorObject=@objTextStream, 
	@strErrorMessage='writing to the file "'+@FileAndPath+'"'
if @HR=0 execute @hr = sp_OAMethod  @objTextStream, 'Write', Null, @string

if @HR=0 Select @objErrorObject=@objTextStream, @strErrorMessage='closing the file "'+@FileAndPath+'"'
if @HR=0 execute @hr = sp_OAMethod  @objTextStream, 'Close'

if @hr<>0
	begin
	Declare 
		@Source varchar(255),
		@Description varchar(255),
		@Helpfile varchar(255),
		@HelpID int
	
	EXECUTE sp_OAGetErrorInfo  @objErrorObject, 
		@source output,@Description output,@Helpfile output,@HelpID output
	Select @strErrorMessage='Error whilst '
			+coalesce(@strErrorMessage,'doing something')
			+', '+coalesce(@Description,'')
	raiserror (@strErrorMessage,16,1)
	end
EXECUTE  sp_OADestroy @objTextStream
EXECUTE sp_OADestroy @objFileSystem