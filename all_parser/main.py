from habr_vacancy import habr_jobs
from hh_vacancy import hh_jobs
# from geekjob import geekjob_jobs
from big_corp import vk_jobs

text = 'python'

with open('base.txt', 'r+', encoding='utf-8') as base:
    base.writelines(f'Habr\n{vac}\n' for vac in habr_jobs(text))
    base.writelines(f'hh\n{vac}\n' for vac in hh_jobs(text))
    # base.writelines(f'GK {vac}\n' for vac in geekjob_jobs(text))
    base.writelines(f'vk\n {vac}\n' for vac in vk_jobs(text))

    
