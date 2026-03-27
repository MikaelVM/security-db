SET ROLE reports_owner;

CREATE TABLE reports.sales_summary_month AS
    SELECT
        count(*) as total_orders,
        sum(unitprice*quantity*(1-discount)) AS total_revenue,
        sum(unitprice*quantity*(discount)) AS total_discount,
        extract(MONTH FROM orderdate) AS sales_month,
        extract(YEAR FROM orderdate) as sales_year
    FROM public.orders JOIN public.orderdetails USING (orderid) GROUP BY sales_month, sales_year
    ORDER BY sales_year, sales_month;

RESET ROLE;
