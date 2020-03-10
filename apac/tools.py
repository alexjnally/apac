def try_to_save(data, name, counter = 1):
    import xlsxwriter
    import os
    import time
    import pandas as pd
    if not isinstance(data, pd.DataFrame):
        raise TypeError('data must be dataframe')

    try:
        s1 = time.time()
        if name[-3:] == 'csv':
            data.to_csv(name)
        elif name[-4:] == 'xlsx':
            data.to_excel(name)
        else:
            name = name + '.csv'
            data.to_csv(name)

        excel_path = 'start EXCEL.EXE ' + name
        os.system(excel_path)
        s2 = time.time()
        stime = s2 - s1
        print('\n========================\nSave File Time:  ' + str(stime)[:4] + ' s\n========================')

    except (xlsxwriter.exceptions.FileCreateError, PermissionError):
        counter += 1
        if name[-3:] == 'csv':
            name = name.replace('.csv', '').replace('_v{}'.format(counter - 1), '') + '_v{}.csv'.format(counter)
        elif name[-4:] == 'xlsx':
            name = name.replace('.xlsx', '').replace('_v{}'.format(counter - 1), '') + '_v{}.xlsx'.format(counter)
        try_to_save(data, name, counter)
        
        
