# Ejemplo en SQL Server 2022

Links de referencia:
* [Instalar SQL Server 2022 en Docker](https://learn.microsoft.com/es-es/sql/linux/quickstart-install-connect-docker?view=sql-server-ver16&pivots=cs1-bash)
* [Descargar la base de datos AdventureWorks2022 en SQL Server 2022](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=tsql)
* [Restaurar una base de datos en un contenedor de SQL Server](https://learn.microsoft.com/es-es/sql/linux/tutorial-restore-backup-in-sql-server-container?view=sql-server-ver16)

Primero es necesario hacer un pull (descargar) la imagen de SQL Server 2022 para Docker.

```bash
sudo docker pull mcr.microsoft.com/mssql/server:2022-latest
```

Luego se debe ejecutar el siguiente comando para crear el contenedor de SQL Server 2022.

```bash
sudo docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=Coder1234" \
    -e "MSSQL_PID=Developer" -e "MSSQL_USER=mssql" \
   -p 1433:1433 --name sql1 --hostname sql1 \
   -d \
   mcr.microsoft.com/mssql/server:2022-latest
```

En este paso se creó el contenedor de SQL Server 2022 con los siguientes parámetros:
* hostname: sql1 (atención si hay que usar en DBeaver localhost o sql1)
* name: sql1 (nombre del contenedor)
* password: Coder1234 (contraseña del usuario SA)
* user: mssql (usuario de la base de datos)
* port: 1433 (puerto de la base de datos)
* db user: SA (usuario de la base de datos para usar en DBeaver)

Crear el directorio de backup y copiar el archivo de backup de la base de datos AdventureWorks2022.bak

```bash
sudo docker exec -it sql1 mkdir /var/opt/mssql/backup
```

```bash
sudo docker cp ./databases/AdventureWorks2022.bak sql1:/var/opt/mssql/backup/AdventureWorks2022.bak
```

<!-- Machete mio, no mostrar en readme
# Attach shell to container with root privileges
sudo docker exec -u 0 -it sql1 bash
cd /var/opt/mssql/backup/
ls -alh
chown mssql:root -R /var/opt/mssql/backup/
chown mssql:mssql -R /var/opt/mssql/data/
chmod 777 -R /var/opt/mssql/backup/
chmod 777 -R /var/opt/mssql/data/
chmod +r /var/opt/mssql/backup/AdventureWorks2022.bak

/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "Coder1234" -->

En DBeaver crear una conexión a la base de datos con los siguientes parámetros:
* host: localhost
* port: 1433
* database: master
* user: SA
* password: Coder1234

Ejecutar el siguiente script para restaurar la base de datos AdventureWorks2022

```sql
USE [master];
GO
RESTORE DATABASE [AdventureWorks2022]
FROM DISK = '/var/opt/mssql/backup/AdventureWorks2022.bak'
WITH
    MOVE 'AdventureWorks2022' TO '/var/opt/mssql/data/AdventureWorks2022.mdf',
    MOVE 'AdventureWorks2022_log' TO '/var/opt/mssql/data/AdventureWorks2022_log.ldf',
    FILE = 1,
    NOUNLOAD,
    STATS = 5;
GO
```

Probar los .sql de la carpeta **Semana_5**. (En DBeaver)

> Query_Lenta_Larga.sql
```sql
USE [AdventureWorks2022];
GO
SET STATISTICS TIME ON
GO
SELECT TOP 25
	Product.ProductID,
	Product.Name AS ProductName,
	Product.ProductNumber,
	CostMeasure.UnitMeasureCode,
	CostMeasure.Name AS CostMeasureName,
	ProductVendor.AverageLeadTime,
	ProductVendor.StandardPrice,
	ProductReview.ReviewerName,
	ProductReview.Rating,
	ProductCategory.Name AS CategoryName,
	ProductSubCategory.Name AS SubCategoryName
FROM Production.Product
INNER JOIN Production.ProductSubCategory
ON ProductSubCategory.ProductSubcategoryID = Product.ProductSubcategoryID
INNER JOIN Production.ProductCategory
ON ProductCategory.ProductCategoryID = ProductSubCategory.ProductCategoryID
INNER JOIN Production.UnitMeasure SizeUnitMeasureCode
ON Product.SizeUnitMeasureCode = SizeUnitMeasureCode.UnitMeasureCode
INNER JOIN Production.UnitMeasure WeightUnitMeasureCode
ON Product.WeightUnitMeasureCode = WeightUnitMeasureCode.UnitMeasureCode
INNER JOIN Production.ProductModel
ON ProductModel.ProductModelID = Product.ProductModelID
LEFT JOIN Production.ProductModelIllustration
ON ProductModel.ProductModelID = ProductModelIllustration.ProductModelID
LEFT JOIN Production.ProductModelProductDescriptionCulture
ON ProductModelProductDescriptionCulture.ProductModelID = ProductModel.ProductModelID
LEFT JOIN Production.ProductDescription
ON ProductDescription.ProductDescriptionID = ProductModelProductDescriptionCulture.ProductDescriptionID
LEFT JOIN Production.ProductReview
ON ProductReview.ProductID = Product.ProductID
LEFT JOIN Purchasing.ProductVendor
ON ProductVendor.ProductID = Product.ProductID
LEFT JOIN Production.UnitMeasure CostMeasure
ON ProductVendor.UnitMeasureCode = CostMeasure.UnitMeasureCode
ORDER BY Product.ProductID DESC;
SET STATISTICS TIME OFF;  
GO  
```

> Query_Optimizada.sql
```sql
SET STATISTICS TIME ON
GO
SELECT TOP 25
	Product.ProductID,
	Product.Name AS ProductName,
	Product.ProductNumber,
	ProductCategory.Name AS ProductCategory,
	ProductSubCategory.Name AS ProductSubCategory,
	Product.ProductModelID
INTO #Product
FROM Production.Product
INNER JOIN Production.ProductSubCategory
ON ProductSubCategory.ProductSubcategoryID = Product.ProductSubcategoryID
INNER JOIN Production.ProductCategory
ON ProductCategory.ProductCategoryID = ProductSubCategory.ProductCategoryID
ORDER BY Product.ModifiedDate DESC;
 
SELECT
	Product.ProductID,
	Product.ProductName,
	Product.ProductNumber,
	CostMeasure.UnitMeasureCode,
	CostMeasure.Name AS CostMeasureName,
	ProductVendor.AverageLeadTime,
	ProductVendor.StandardPrice,
	ProductReview.ReviewerName,
	ProductReview.Rating,
	Product.ProductCategory,
	Product.ProductSubCategory
FROM #Product Product
INNER JOIN Production.ProductModel
ON ProductModel.ProductModelID = Product.ProductModelID
LEFT JOIN Production.ProductReview
ON ProductReview.ProductID = Product.ProductID
LEFT JOIN Purchasing.ProductVendor
ON ProductVendor.ProductID = Product.ProductID
LEFT JOIN Production.UnitMeasure CostMeasure
ON ProductVendor.UnitMeasureCode = CostMeasure.UnitMeasureCode;
 
DROP TABLE #Product;
SET STATISTICS TIME OFF;  
GO  
```

Por último, parar el contenedor de SQL Server 2022.

```bash
sudo docker stop sql1
```

Y eliminarlo.

```bash
sudo docker rm sql1
```