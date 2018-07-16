import math
modeldict={
    'fv':'final value',
    'iv':'initial value',
    'dr':'decay rate',
    'gs':'global step',
    'ds':'decay step'
    }
info0 = ['Please select target:','fv : final value','iv : initial value','dr : decay rate','gs : global step','ds : decay step','------q/Q to quit------']
info1 = ['final value: ','initial value: ','decay rate: ','global step: ','decay step: ']
while True:
    for i in info0:
        print(i)
    fv=0.
    iv=0.
    dr=0.
    gs=0.
    ds=0.
    try:
        target=input()
        if target=='fv':
            iv=eval(input(info1[1]))
            dr=eval(input(info1[2]))
            gs=eval(input(info1[3]))
            ds=eval(input(info1[4]))
            fv=(dr**(gs/ds))*iv
            print('====final value : ',fv,'====')
            print('')
            print('')
            print('')

        elif target=='iv':
            fv=eval(input(info1[0]))
            dr=eval(input(info1[2]))
            gs=eval(input(info1[3]))
            ds=eval(input(info1[4]))
            iv=fv/(dr**(gs/ds))
            print('====initial value : ',iv,'====')
            print('')
            print('')
            print('')
        elif target=='dr':
            fv=eval(input(info1[0]))
            iv=eval(input(info1[1]))
            gs=eval(input(info1[3]))
            ds=eval(input(info1[4]))
            dr=(fv/iv)**(ds/gs)
            print('====decay rate : ',dr,'====')
            print('')
            print('')
            print('')
        elif target=='gs':
            fv=eval(input(info1[0]))
            iv=eval(input(info1[1]))
            dr=eval(input(info1[2]))
            ds=eval(input(info1[4]))
            gs=ds*(math.log(fv/iv)/math.log(dr))
            print('====global step : ',gs,'====')
            print('')
            print('')
            print('')
        elif target=='ds':
            fv=eval(input(info1[0]))
            iv=eval(input(info1[1]))
            dr=eval(input(info1[2]))
            gs=eval(input(info1[3]))
            ds=gs*(math.log(dr)/math.log(fv/iv))
            print('====decay step : ',ds,'====')
            print('')
            print('')
            print('')
        elif target=='q' or target=='Q':
            break
        else:
            print('')
            print('')
            print('')
            print('Please make a right choice!')
            print('')
            print('')
            print('')
    except Exception as e:
        print('')
        print('')
        print('')
        print('error!!!')
        print(e)
        print('')
        print('')
        print('')
        pass
