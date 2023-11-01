select rin_category, sum(case when smw_max_voltage >= 33 then 1 else 0 end) "Subtransmission Poles"
      ,sum(case when nvl(smw_max_voltage,11) between 5 and 22 then 1 else 0 end) "Distribution Poles"
      ,sum(case when smw_max_voltage < 5 and smw_pole_type not in ('SL','Bollard') then 1 else 0 end) "LV poles"
      ,sum(case when smw_max_voltage < 5 and smw_pole_type in ('SL','Bollard') then 1 else 0 end) "Streetlights/Bollards"
      ,count(*) "All Poles"
from   pole_cv po
where  po_equip_class = 'PO'
and    po_equip_status in ('PR', 'IS')
and    po_equip_grp_id in ('G-POLEWOOD','G-POLECONC','G-POLESTEEL')
and    ns_equip_grp_id = 'S-NSPOLE    '
and    nvl(trim(ns_equip_classifx6),'ER') = 'ER'
and    ns_equip_status not in ('BD','DI','DE')
and    nvl(smw_pole_order,1) = 1 -- Only get 1 record for Smallworld poles with duplicate Ecorp IDs
and    nvl(po_pole_order,1) = 1 -- Only get 1 record for multiple Ellipse physicals with the same parent site
and    po_asset_regulated is null -- Exclude isolated and unregulated network
group by rin_category;