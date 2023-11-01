import os
import sys
from datetime import datetime, timedelta as td
import pytz

bris_str = 'Australia/Brisbane'
sydn_str = 'Australia/Sydney'
sing_str = 'Asia/Singapore'
lond_str = 'Europe/London'
san_fran_str = 'America/Los_Angeles'
toro_str = 'America/Toronto'
sanpaulo_str = 'America/Sao_Paulo'
amst_str = 'Europe/Amsterdam'
dubai_str = 'Asia/Dubai'

bris = pytz.timezone(bris_str)
sydn = pytz.timezone(sydn_str)
sing = pytz.timezone(sing_str)
lond = pytz.timezone(lond_str)
toto = pytz.timezone(toro_str)
san_fran = pytz.timezone(san_fran_str)
san_paulo = pytz.timezone(sanpaulo_str)
amst = pytz.timezone((amst_str))
dubi = pytz.timezone((dubai_str))

def request_tz(cmp_loc,d_obj):
    if cmp_loc == bris_str:
        return (bris.localize(d_obj))
    elif cmp_loc == sydn_str:
        return (sydn.localize(d_obj))
    elif cmp_loc == sing_str:
        return (sing.localize(d_obj))
    elif cmp_loc == lond_str:
        return (lond.localize(d_obj))
    elif cmp_loc == san_fran_str:
        return (san_fran.localize(d_obj))
    elif cmp_loc == toro_str:
        return (toto.localize(d_obj))
    elif cmp_loc == sanpaulo_str:
        return (san_paulo.localize(d_obj))
    elif cmp_loc == amst_str:
        return (amst.localize(d_obj))
    elif cmp_loc == dubai_str:
        return (amst.localize(d_obj))
    else:
        print("Typo Error")

""" How to derive numeric values for Year, Month, Day, Hour and minute  
current_time = datetime.now()
yr = current_time.year
mth_of = current_time.month
day_of = current_time.day
hr = current_time.hour
mm = current_time.minute
cmp_loc = bris_str
"""

MANUALLY_SET = False

""" For international Appointments - manually set them (Patty) ***
yr = 2023
mth_of = 9
day_of = 7
hr = 13
mm= 0
cmp_loc = san_fran_str
MANUALLY_SET = True
"""

if MANUALLY_SET == True:
    dt_obj = datetime(yr, mth_of, day_of, hr, mm)
else:
    dt_obj = datetime.now()
    cmp_loc = bris_str

dt_obj = request_tz(cmp_loc,dt_obj)

# Print All
qld_time = dt_obj.astimezone(bris)
print(f'\nQueensland Time :{qld_time.strftime("%d-%m-%Y %H:%M")}')

print("\nNormally daylight saving is taken into consideration \n\tbut change overs might look odd is comparing it to your phone and a different date. \n")

lond_time = dt_obj.astimezone(lond)
print(f'London Time :{lond_time.strftime("%d-%m-%Y %H:%M")}')

toto_time = dt_obj.astimezone(toto)
print(f'Toronto Time :{toto_time.strftime("%d-%m-%Y %H:%M")}')

sanf_time = dt_obj.astimezone(san_fran)
print(f'San Franciso Time :{sanf_time.strftime("%d-%m-%Y %H:%M")}')

sanp_time = dt_obj.astimezone(san_paulo)
print(f'San Paulo Time :{sanp_time.strftime("%d-%m-%Y %H:%M")}')

print('\n\tExtra - for Travellers')
amst_time = dt_obj.astimezone(amst)
print(f'Amsterdam :{amst_time.strftime("%d-%m-%Y %H:%M")}')

dubi_time = dt_obj.astimezone(dubi)
print(f'Dubai :{dubi_time.strftime("%d-%m-%Y %H:%M")}')

