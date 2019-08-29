import subprocess, json

output_str = str(subprocess.check_output('last reboot', shell=True))
lines = output_str.split('reboot')
os_base = str(subprocess.check_output('uname -s', shell=True))	
	
months_macos = json.loads(open('json/months.json', 'r').read())
days_macos = json.loads(open('json/days_of_week.json', 'r').read())
	
txt_tmplt = json.loads(open('json/text.json', 'r').read())	
	
langs = ['eng', 'pl']	
os_av = {
	'Darwin': {
		'months': months_macos,
		'days': days_macos
	},
	'Linux': {
		'months': None, # available soon
		'days': None    # available soon
	}
}
lang_chsn = 'eng'
	
def parse_line(line_index):
	txt_parts = txt_tmplt['report_parts'][lang_chsn]

	line_parts = lines[line_index].split()
	day_of_week = line_parts[1]
	month = line_parts[2]
	day_of_month = line_parts[3]
	boot_time = line_parts[4]
	return txt_parts[0] + trnsl_month(month) + txt_parts[1] + day_of_month + txt_parts[2] + trnsl_day(day_of_week) + txt_parts[3] + boot_time

def trnsl_month(month):
	return os_av[os_base[2:-3]]['months'][month.lower()][lang_chsn]
		
def trnsl_day(day_of_week):
	return os_av[os_base[2:-3]]['days'][day_of_week.lower()][lang_chsn]

def display_all():
	for index in range(1, len(lines)):
		parse_rslt = parse_line(index)
		print(parse_rslt)

display_all()
	
	
	