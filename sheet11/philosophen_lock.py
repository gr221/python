import multiprocessing as m
import time

def essen(i, gabeln, teller,sperre):
    while(teller[i] != 0):
        if gabeln[i-1] == 1 and gabeln [(i+1)%5] == 1:
            sperre.aquire()
            print("Philosoph", i , "versucht Gabeln zu nehmen.")
            time.sleep(0.2)
            gabeln[i-1] = 0
            time.sleep(0.2)
            gabeln[(i+1)%5] = 0
            sperre.release()
            if gabeln[i-1] == 0 and gabeln [(i+1)%5] == 0:
                time.sleep(0.2)
                teller[i] -= 1
                print("Philosoph",i, "hat eine Gabel gegessen.")
                time.sleep(0.2)
                gabeln[i-1] = 1
                time.sleep(0.2)
                gabeln[(i+1)%5] = 1
                print("Philosoph", i, "hat Gabeln zurückgelegt und noch" ,\
                        teller[i], "Portionen vor sich.")
        else :
            print("Philosoph ", i, " sagt schlaue Dinge.")
    print("Philosoph ", i, " hat aufgegessen.")


def main():
    philosophen = []
    gabeln = m.Array('i',[1,1,1,1,1])
    teller = m.Array('i',[5,5,5,5,5])
    sperre = m.Lock()
    for i in range(5):
        philosophen.append(m.Process(target=essen, args=(i,gabeln,teller,sperre)))

    for p in philosophen:
        p.start()
    for p in philosophen:
        p.join()



if __name__=="__main__":
    main()

