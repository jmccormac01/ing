#########################################################
#   v1.4   06/08/13  -  Fixed bug in saturating behaviour - JMCC PRS 
#   v1.5   16/08/13  -  Added am/pm_tweaks of 0.9 and 1.1, upped max counts to 40,000  
#                       Added PRS's subprocesses - needs tested on ICS 
#                       Added summary of all successfull flats printed at the end - JMCC
#					
#   Add comments to headers?
def subP(comm):
	p = subprocess.Popen(comm, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
	return p
		p=subP('rspeed %s fast' % camera_name)
		os.system('bias %s' % camera_name)
		os.system('bias %s' % camera_name)
	
	req_exp=test_time/(sky_lvl/target_counts)
	
	# if within limits, fine
	if sky_lvl <= 64000:		
	
	# if outside limits afternoon and morning need done differently
	if token == 1:
	
	# if within limits, fine. if not then morning and afternoon need handled differently	
	if sky_lvl <= 64000:
	if token == 1:
# a list for filter name, image number and median counts to print summary at the end
filt_summ, im_summ, med_sum = [],[],[]
	
				p=subP('window acam 1 "[875:1275,1850:2250]"')
				p=subP('rspeed acam fast')
				
		
				# catch error?	
						# append filter, name and sky level to summary lists 
						filt_summ.append(filt_seq[i])
						im_summ.append(t)
						med_summ.append(sky_lvl)
						
				p=subP('window acam 1 "[875:1275,1850:2250]"')
				p=subP('rspeed acam fast')
					# catch error?
				# catch error?
						# append filter, name and sky level to summary lists 
						filt_summ.append(filt_seq[i])
						im_summ.append(t)
						med_summ.append(sky_lvl)
						
	# print out the summary
	if len(filt_summ) == len(im_summ) == len(med_summ):
		print("\n\n------------------------------")
		print("\tAutoflat Summary")
		print("------------------------------\n")
		for i in range(0,len(filt_summ)):
			print("%s   %s   %s" % (filt_summ[i],im_summ[i],med_summ[i]))
		print('\n\n')
			
	