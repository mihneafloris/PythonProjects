import math
length  = 0.9
mass = 5.0
width = 0.05

sheetmaterials = {"carbon": {"E": 42.5 , "rho":1470},"aluminium": {"E": 72.4 , "rho":2780},"steel": {"E": 200 , "rho":7850}}
corematerials = {"aramide": {"E": 1.118 , "rho":82},"aluminium": {"E": 1.118 , "rho":82}, "foam": {"E": 4.16 , "rho":100}}

def optimumcalc(sheet, core):
    options = []
    t_c = 0.00025
    
    while t_c < 0.1:
        f_n = 0
        t_s = 0.0001
        I_c = (width*(t_c**3))/12
        while f_n < 25.0:
            I_s = 2*((width*(t_s**3))/12+t_s*width*(((t_c+t_s)/2)**2))
            f_n = math.sqrt( (48*(10**9)*( sheetmaterials[sheet]['E']*I_s + corematerials[core]['E']*I_c)) / (mass*(length**3)) )/(2*math.pi)
            t_s += 0.0001
        #print(t_c, t_s, f_n)
        beammass = width*length*(t_s*sheetmaterials[sheet]['rho'] + t_c*corematerials[core]['rho'])
        options.append([t_s, t_c, f_n, beammass])
        t_c += 0.0005
    
    minmass = 1000.0
    index = 0
    for i in range(len(options)):
        if options[i][3] <=minmass:
            index = i
            minmass = options[i][3]
    return options[index]

def main():
    name = input("Enter name of run: ")
    #sheet = input("input sheet material {'carbon', 'aluminium', 'steel'}: ")
    #core = input("input core material {'aramide', 'aluminium', 'foam'}: ")

    results = []

    print("carbon - aramide")
    results.append(["carbon - aramide", optimumcalc("carbon","aramide")])
    print(results[-1])

    print("carbon - foam")
    results.append(["carbon - foam", optimumcalc("carbon","foam")])
    print(results[-1])

    print("aluminium - aramide")
    results.append(["aluminium - aramide", optimumcalc("aluminium","aramide")])
    print(results[-1])

    print("aluminium - aluminium")
    results.append(["aluminium - aluminium",optimumcalc("aluminium","aluminium")])
    print(results[-1])
    
    print("steel - aluminium")
    results.append(["steel - aluminium", optimumcalc("steel","aluminium")])
    print(results[-1])

    file1  = open(name + ".txt", 'w')
    csvfile = open(name + ".csv", 'w')
    for res in results:
        string = '{0}: t_s= {1:1.6f}, t_c= {2:1.6f}, F_n= {3:1.6f}, m= {4:1.6f} \n'.format(res[0], res[1][0], res[1][1], res[1][2],res[1][3])
        string2 = '{0},{1:1.6f},{2:1.6f},{3:1.6f},{4:1.6f} \n'.format(res[0], res[1][0], res[1][1], res[1][2],res[1][3])
        print(string)
        file1.write(string)
        csvfile.write(string2)
    file1.close()
    csvfile.close()



if __name__ == "__main__":
    main()