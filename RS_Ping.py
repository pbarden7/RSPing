import re
from subprocess import Popen, PIPE
worlds = {
'oldschool5.runescape.com':'World 305',
'oldschool6.runescape.com':'World 306',
'oldschool7.runescape.com':'World 307',
'oldschool13.runescape.com':'World 313',
'oldschool14.runescape.com':'World 314',
'oldschool15.runescape.com':'World 315',
'oldschool19.runescape.com':'World 319',
'oldschool20.runescape.com':'World 320',
'oldschool21.runescape.com':'World 321',
'oldschool22.runescape.com':'World 322',
'oldschool23.runescape.com':'World 323',
'oldschool24.runescape.com':'World 324',
'oldschool29.runescape.com':'World 329',
'oldschool30.runescape.com':'World 330',
'oldschool31.runescape.com':'World 331',
'oldschool32.runescape.com':'World 332',
'oldschool38.runescape.com':'World 338',
'oldschool39.runescape.com':'World 339',
'oldschool40.runescape.com':'World 340',
'oldschool46.runescape.com':'World 346',
'oldschool47.runescape.com':'World 347',
'oldschool48.runescape.com':'World 348',
'oldschool53.runescape.com':'World 353',
'oldschool54.runescape.com':'World 354',
'oldschool55.runescape.com':'World 355',
'oldschool56.runescape.com':'World 356',
'oldschool57.runescape.com':'World 357',
'oldschool61.runescape.com':'World 361',
'oldschool62.runescape.com':'World 362',
'oldschool74.runescape.com':'World 374',
'oldschool77.runescape.com':'World 377',
'oldschool78.runescape.com':'World 378',
'oldschool115.runescape.com':'World 415',
'oldschool116.runescape.com':'World 416',
'oldschool120.runescape.com':'World 420',
'oldschool121.runescape.com':'World 421',
'oldschool122.runescape.com':'World 422',
'oldschool128.runescape.com':'World 428',
'oldschool129.runescape.com':'World 429',
'oldschool143.runescape.com':'World 443',
'oldschool144.runescape.com':'World 444',
'oldschool145.runescape.com':'World 445',
'oldschool146.runescape.com':'World 446',
'oldschool177.runescape.com':'World 477',
'oldschool178.runescape.com':'World 478',
'oldschool179.runescape.com':'World 479',
'oldschool180.runescape.com':'World 480',
'oldschool181.runescape.com':'World 481',
'oldschool182.runescape.com':'World 482',
'oldschool184.runescape.com':'World 484',
'oldschool185.runescape.com':'World 485',
'oldschool186.runescape.com':'World 486',
'oldschool187.runescape.com':'World 487',
'oldschool188.runescape.com':'World 488',
'oldschool189.runescape.com':'World 489',
'oldschool190.runescape.com':'World 490',
'oldschool191.runescape.com':'World 491',
'oldschool192.runescape.com':'World 492',
'oldschool193.runescape.com':'World 493',
'oldschool194.runescape.com':'World 494',
'oldschool195.runescape.com':'World 495',
'oldschool196.runescape.com':'World 496'
}

def worldLatency(servers):
    returnlist = {}
    #find the ping from each world
    for host, worldnum in servers.items():
        stdout = Popen('ping -n 1 ' + host, shell=True, stdout=PIPE).stdout
        output = str(stdout.read())
        if 'timed out' in output:
            continue
        latency = re.findall("(?<=Minimum = )[0-9]{2,}", output)
        intlatency = int(latency[0])

        #worlds with latency under 40 ms are returned
        if intlatency < 40:
            returnlist.update({worldnum:intlatency})
            
    return returnlist

#output dictionary, this is unsorted
output1 = worldLatency(worlds)

#sorting the output by latency
output2=dict(sorted(output1.items(),key= lambda x:x[1]))

    

#printing the sorted dictionary
for x, y in output2.items():
    print(x + ': ' + str(y) + 'ms')
