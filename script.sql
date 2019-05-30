select x.*, concat(x.orderno,'-',y.ticket_cnt) ticket_code
from (
	select b.accountid, sc.client_name, cb.date_applied, cb.orderno, cb.billamount, pi.ticket_type, sp.pos_name, sp.pos_code
	from (select cfborroworderid id, upper(snorimei) ticket_type
		from Cashacart_PurchaseInfo
		where snorimei like '%b2s%'
		) pi
	left join (select id, orderno, billamount, storeid, date(createdat) date_applied
		from Cashacart_CF_Borroworders
		where createdat >= date'2019-05-28'
		) cb
		on pi.id = cb.id
	left join (select orderno, accountid
		from Cashacart_Borroworders
		) b
		on cb.orderno = b.orderno
	left join (select id, name pos_name,code pos_code from Cashacart_Sales_POS
		) sp
		on cb.storeid = sp.id
	left join (select accountid,
		replace(concat(firstname,' ',middlename,' ',lastname),'  ',' ') client_name
		from Cashacart_Sales_Client 
		) sc
		on b.accountid = sc.accountid
	group by cb.orderno
    ) x
left join (select 1 as ticket_cnt
	union select 2 as ticket_cnt
    union select 3 as ticket_cnt
    union select 4 as ticket_cnt
    union select 5 as ticket_cnt
    union select 6 as ticket_cnt
    union select 7 as ticket_cnt
    union select 8 as ticket_cnt
    union select 9 as ticket_cnt
    union select 10 as ticket_cnt
    ) y
    on case when x.ticket_type = 'B2S' then truncate(x.billamount/2500,0) >= y.ticket_cnt
        else truncate(x.billamount/2500,0)*2 >= y.ticket_cnt
        end