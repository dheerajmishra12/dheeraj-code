import logging
logging.basicConfig(filename = "test.log" ,level = logging.INFO)
logging.info("log this line of executation")
logging.debug("this is my msg")
logging.warning("this is warning msg")
logging.error("this is my error") 
logging.critical("this is my critical")
# 1.NOTSET 
# 2.DEBUG 
# 3. INFO 
# 4. WARNING 
# 5. ERROR 
# 6. CRITICAL

logging.shutdown() 

import logging

logging.basicConfig(filename = "test1.log" ,level = logging.DEBUG ,format = "%(asctime)s %(message)s"   ) 
logging.info("this is my info logging") 
logging.error("this is my error") 
logging.critical("this is my critical") 
logging.shutdown() 
import logging 
logging.basicConfig(filename = "test2.log" , level = logging.DEBUG , format = '%(asctime)s %(name)s %(levelname)s  %(message)s')
logging.info("this is my info") 
logging.critical("this is my critical for test2 file") 
l = [1,2,3,34,4,[2,3,4] , "dhee" , "kumar"]
l1_int = []
l2_str = []
for i in l :
    logging.info("we are iterating throuhg our list and our local var is {}".format(l ))
    if type(i ) == list :
        logging.info("i am inside if statement and i am trying to check list type" + str(i))
        for j in i :
            logging.info("i am in anothe for loop for list inside list element "+ str(j))
            if type(j) == int :
                logging.info("i am inside if statement")
                l1_int.append(j)
    elif type(i) == int :
        l1_int.append(i)
    else :
        if type(i) == str :
            l2_str.append(i)
logging.info("my final result for int is {l1} and str is {l2}".format(l1 =l1_int , l2 = l2_str ))