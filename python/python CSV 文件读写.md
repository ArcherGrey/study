# python CSV 文件读写（python 2.7）


> CSV 格式是最常见的用来导入导出电子表格和数据库的格式。不过没有一个确定的标准，都是根据具体使用的应用来定义相对的标准。由于缺乏一个标准所以在不同的应用读写数据可能会产生不同的结果。不过虽然会有小的差异但是大体上格式都很类似。

注：这个版本的 csv 模块不支持 Unicode 的输入，所有的输入必须是 UTF-8 或者 可以打印的 ASCII。

## 模块内容
CSV 模块定义了下面的函数：


> csv.reader(csvfile, dialect='excel', **fmtparams)

 `csvfile` 可以是文件对象也可以是 `list` 对象，如果是文件对象的话需要加一个 `b` 标志位来区别。 `dialect` 作为一个可选参数，编码风格，默认为excel方式，也就是逗号(`,`)分隔，另外csv模块也支持excel-tab风格，也就是制表符(`tab`)分隔。其它的方式需要自己定义，然后可以调用register_dialect方法来注册，以及list_dialects方法来查询已注册的所有编码风格列表。最后一个参数是格式化参数，用来覆盖之前dialect对象指定的编码风格。

例：

    >>> import csv
    >>> with open('eggs.csv', 'rb') as csvfile:
    ...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    ...     for row in spamreader:
    ...         print ', '.join(row)
    Spam, Spam, Spam, Spam, Spam, Baked Beans
    Spam, Lovely Spam, Wonderful Spam

> csv.writer(csvfile, dialect='excel', **fmtparams)

同上
例：

    import csv
    with open('eggs.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])



> csv.register_dialect(name, [dialect, ]**fmtparams)

注册一种风格。



> csv.unregister_dialect(name)

删除已注册的风格。



> csv.get_dialect(name)

返回对于名称的编码风格



> csv.list_dialects()

返回所有编码风格的名称



>  csv.DictReader(csvfile, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)

和 `reader` 差不多，不过返回的是字典类型。
例：

    >>> import csv
    >>> with open('names.csv') as csvfile:
    ...     reader = csv.DictReader(csvfile)
    ...     for row in reader:
    ...         print(row['first_name'], row['last_name'])
    ...
    Baked Beans
    Lovely Spam
    Wonderful Spam、

> csv.DictWriter(csvfile, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)

同上
例：

    import csv

    with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})