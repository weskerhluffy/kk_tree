'''
Created on 19/09/2017

@author: 
'''
import logging
import sys
nivel_log = logging.ERROR
#nivel_log = logging.DEBUG
logger_cagada = None

def kk_tree_core(n, k, d):
    dp = [0] * (n + 1)
    dp_grande = [0] * (n + 1)
    dp[0] = 1
    dp_grande[0] = 1
    num_formas = 0
    for tam_casilla in range(1, n - d + 1):
        logger_cagada.debug("en tam casilla {}".format(tam_casilla))
        for num_act in range(1, d):
            if(num_act > tam_casilla):
                break
            resto = tam_casilla - num_act
            logger_cagada.debug("num act {} resto {}".format(num_act, resto))
            dp[tam_casilla] += dp[resto]
    logger_cagada.debug("la dp es {}".format(dp))
    dp[0] = 0
    for tam_casilla in range(d, n + 1):
        logger_cagada.debug("el tam casilla g {}".format(tam_casilla))
        for num_act in range(1, k + 1):
            if(num_act > tam_casilla):
                break
            resto = tam_casilla - num_act
            if(resto < d and num_act < d):
                continue
            logger_cagada.debug("num act g {} resto {}".format(num_act, resto))
            num_formas_chicas = dp[resto] if num_act >= d else 0
            num_formas_grandes = dp_grande[resto]
            logger_cagada.debug("num formas chicas {} grandes {}".format(num_formas_chicas, num_formas_grandes))
            dp_grande[tam_casilla] += num_formas_chicas + num_formas_grandes
    logger_cagada.debug("la dp grande  es {}".format(dp_grande))
    
    num_formas = dp_grande[n]
        
    return num_formas%(1000000007)   

def kk_tree_main():
    lineas = list(sys.stdin)
    n, k, d = [int(x) for x in lineas[0].strip().split(" ")]
    resu = kk_tree_core(n, k, d)
    print("{}".format(resu))

if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)
        kk_tree_main()
