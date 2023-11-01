/* 

STD_JOB_NO,STD_JOB_DESC,MAINT_TYPE,WO_JOB_CODEX10
AIE1X ,EARTH TESTING SWER- PINS                ,MP,01   
AIA1X ,ABS INSPECTIONS/MAINTENANCE - PINS      ,MP,01   
AIP4X ,POLE TOP INSPECTIONS - PINS             ,MP,01   
AILPX ,STREET LIGHT PATROL - PINS              ,MP,01   
AILBX ,BULK LAMP REPLACEMENT - PINS            ,MP,01   
AIATX ,ACCESS TRACK - PINS                     ,MP,01   
AIP1X ,ABOVE GROUND INSPECTIONS - PINS         ,MP,01   
AIP2X ,GROUNDLINE INSPECT DC MODE - PINS       ,MP,01   
AIP3X ,GROUNDLINE INSPECTIONS - PINS           ,MP,01   
AIE2X ,EARTH TESTING NON SWER - PINS           ,MP,01   
AILCX ,BULK LAMP & PE CELL REPLACEMENT - PINS  ,MP,01   
AIP5X ,LEVEL 2 SERVICEABILITY ASSESSMENT - PINS,MP,01   

*/

 
DROP TABLE MP_Status_Poles;
COMMIT; 

Create Table MP_Status_Poles as (
SELECT w.work_order, w.std_job_no, w.closed_status, w.wo_job_codex10, w.equip_no,
       w.plan_str_date, w.plan_fin_date, w.CLOSED_DT, e.Plant_no, substr(e.Plant_no,4) Z_Opid, e.item_name_1, 'PYRL' Status, 0 EEPoles_Qty,
       (w.plan_fin_date - w.plan_str_date ) Days_allocated, to_char(( sysdate - w.plan_fin_date ), '99999') Days_Late
  FROM ellipse.msf620 w,
       ellipse.msv600 e
 WHERE w.EQUIP_NO = e.EQUIP_NO
   AND w.std_job_no = 'AIP3X'
   AND w.wo_job_codex10 = '01'
   AND w.plan_str_date < '1-JUL-2008'
   AND w.plan_fin_date < to_char(sysdate, 'DD-Mon-YYYY')
   AND w.CLOSED_STATUS = ' ' );

COMMIT; 


-- Last years but still being worked on. 
Insert into MP_Status_Poles  (
SELECT w.work_order, w.std_job_no, w.closed_status, w.wo_job_codex10, w.equip_no,
       w.plan_str_date, w.plan_fin_date, w.CLOSED_DT,  e.Plant_no, substr(e.Plant_no,4) Z_Opid, e.item_name_1, 'PYCO' Status, 0 EEPoles_Qty,
       (w.plan_fin_date - w.plan_str_date ) Days_allocated, 0 Days_Late
  FROM ellipse.msf620 w,
       ellipse.msv600 e
 WHERE w.EQUIP_NO = e.EQUIP_NO
   AND w.std_job_no = 'AIP3X'
   AND w.wo_job_codex10 = '01'
   AND w.plan_str_date < '1-JUL-2008'
   AND w.plan_fin_date >= to_char(sysdate, 'DD-Mon-YYYY')
   AND w.CLOSED_STATUS = ' ' );

COMMIT; 


-- ****


-- Current Year and Late 
Insert into MP_Status_Poles  (
        SELECT w.work_order, w.std_job_no, w.closed_status, w.wo_job_codex10, w.equip_no,
               w.plan_str_date, w.plan_fin_date, w.CLOSED_DT, e.Plant_no, substr(e.Plant_no,4) Z_Opid, e.item_name_1, 'CYLA' Status, 0 EEPoles_Qty,
               (w.plan_fin_date - w.plan_str_date ) Days_allocated, to_char(( sysdate - w.plan_fin_date ), '99999') Days_Late
          FROM ellipse.msf620 w,
               ellipse.msv600 e
         WHERE w.EQUIP_NO = e.EQUIP_NO
           AND w.std_job_no = 'AIP3X'
           AND w.wo_job_codex10 = '01'
           AND w.CLOSED_STATUS = ' ' 
           AND w.plan_str_date between '1-JUL-2008' AND '30-JUN-2009'
           AND w.plan_fin_date < to_char(sysdate, 'DD-Mon-YYYY'));
           
COMMIT; 

-- Current Year and Not Late 
Insert into MP_Status_Poles  (
        SELECT w.work_order, w.std_job_no, w.closed_status, w.wo_job_codex10, w.equip_no,
               w.plan_str_date, w.plan_fin_date, w.CLOSED_DT, e.Plant_no, substr(e.Plant_no,4) Z_Opid, e.item_name_1, 'CYOS' Status, 0 EEPoles_Qty,
               (w.plan_fin_date - w.plan_str_date ) Days_allocated, 0 Days_Late
          FROM ellipse.msf620 w,
               ellipse.msv600 e
         WHERE w.EQUIP_NO = e.EQUIP_NO
           AND w.std_job_no = 'AIP3X'
           AND w.wo_job_codex10 = '01'
           AND w.CLOSED_STATUS = ' ' 
           AND w.plan_str_date between '1-JUL-2008' AND '30-JUN-2009'
           AND w.plan_fin_date >= to_char(sysdate, 'DD-Mon-YYYY'));  

-- Current Year and Closed 
   
Insert into MP_Status_Poles  (
        SELECT w.work_order, w.std_job_no, w.closed_status, w.wo_job_codex10, w.equip_no,
               w.plan_str_date, w.plan_fin_date, w.CLOSED_DT, e.Plant_no, substr(e.Plant_no,4) Z_Opid, e.item_name_1, 'CYCD' Status, 0 EEPoles_Qty,
               (w.plan_fin_date - w.plan_str_date ) Days_allocated, to_char(( w.CLOSED_DT - w.plan_fin_date ), '99999') Days_Late
          FROM ellipse.msf620 w,
               ellipse.msv600 e
         WHERE w.EQUIP_NO = e.EQUIP_NO
           AND w.std_job_no = 'AIP3X'
           AND w.wo_job_codex10 = '01'
           AND w.CLOSED_STATUS = 'C' -- closed 
           AND plan_str_date between '1-JUL-2008' AND '30-JUN-2009');
 
COMMIT;


Create index MPP_ENO ON mp_status_poles (Equip_no);

COMMIT;

/* Formatted on 2008/09/18 16:05 (Formatter Plus v4.8.8) */
UPDATE mp_status_poles m
   SET m.eepoles_qty =
           (SELECT attrib_value_num_9
              FROM ellipse.msv6a4 n
             WHERE n.equip_no = m.equip_no AND attribute_name = 'NO_EE_POLES');
             
COMMIT;
/*
select status, count(status) 
from MP_Status_Poles
group by status;
*/


drop Table MP_STATUS_Poles_Geom ;

create Table MP_STATUS_Poles_Geom as (
select m.* , z.geom, 'Dist' Type
from MP_STATUS_POLES m,
     IZ_DIST z
where lpad(z.Oper_no,7) = lpad(m.Z_OPID,7));


INsert into MP_Status_poles_Geom ( 
select m.* , z.geom, 'Tran' Type
from MP_STATUS_POLES m,
     IZ_TRAn z
where lpad(z.Oper_no,7) = lpad(m.Z_OPID,7));

Commit;

