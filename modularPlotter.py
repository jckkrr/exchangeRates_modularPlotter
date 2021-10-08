def SlightlyWide(n):    # n == number of subplots

    import pandas as pd
    from IPython.display import display

    columns=['cols','rows','full_rows','extra_row_cols','subplots','col_rows_diff']

    df = pd.DataFrame(columns=columns)

    for i in range(1,n):

        cols = i

        full_rows = n//i
        extra_row = 1 if n%i != 0 else 0
        rows = full_rows + extra_row

        extra_row_cols = n%i

        subplots = cols * full_rows + extra_row_cols

        col_rows_diff = cols-rows
        
        df.loc[i,columns] = [cols,rows,full_rows,extra_row_cols,subplots,col_rows_diff]

    min_diff = df.loc[df['col_rows_diff'] >= 0, 'col_rows_diff'].min()
    
    df = df.loc[df['col_rows_diff'] == min_diff]
    
    cols = df['cols'].item()
    rows = df['rows'].item()
    
    #display(df.style.hide_index())
    
    return cols, rows