USE [TscInsHomeTest]
GO
/****** Object:  StoredProcedure [dbo].[SP_GetOnlineFileExcelList]    Script Date: 8/16/2018 5:25:25 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[SP_GetOnlineFileExcelList] 
AS
BEGIN

SET NOCOUNT ON

/*

online credit card payment 
  select all policies that meet all these conditions
    1. inforce policy 
    2. balance >= 0
    3. not ACH account
    4. not mortgage payment
    
  record layout
     policy# (Symbol, Account#, Suffix)
     Policy Effective date (YYYYMMDD)
     Applicant Name
     Zip Code
     Total Amount Due
     Current Amount Due
     Last Paid Amount
     Last Paid Date (YYYYMMDD)

*/

select 'AHO' + dbo.F_GetValidPolicyNumber(p.PolicyNumber), 
   dbo.F_FormatDateYYYMMDD(p.EffectiveDate),
   q.firstname + ' ' + q.LastName,
   z.zipcode, dbo.F_Fin_GetPayOff(p.policynumber),
   e.PaymentAmount - isnull(m.CurrentCredits,0) + isnull(m.CurrentLateFees,0),
   dbo.F_GetLastAmountPaid(p.PolicyNumber),
   dbo.F_GetLastDatePaid(p.PolicyNumber)
   from policy p (nolock) join Address a on a.id = p.HomeAddressPTR 
   join ZipInfo z on z.id = a.ZipInfo_ZipInfoPTR 
   join Person q on q.ID = p.PolicyHolderPersonPTR 
   join FinanceMaster m on m.PolicyNumber = p.PolicyNumber 
   join FinancePayment e on e.ContractPTR = m.CurrentContractPTR and e.PaymentNumber = m.NextPaymentNumber 
   where policystatusid in (1,3) and p.expirationdate > getdate() and p.effectivedate < getdate()
   and Not exists (select r.id from Policy r where r.QuoteNumber = p.QuoteNumber 
      and r.PolicyStatusID in (1,3) and r.ID > p.ID)
   --and m.FinanceStatusID in (1,3)    
   and not exists (select * from noticehistory n where n.policynumber = p.policynumber and n.rescindeddate is null and n.canceldate < getdate())
   and dbo.F_Fin_GetPayOff(p.policynumber) >= 0
   and ISNULL(m.AutoDraft_Enabled,0) = 0 
   and ISNULL(p.FinancePlanID,0) <> 6

END
