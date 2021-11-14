#
#
# create table items(
# item_id serial primary key,
# name varchar(50),
# price int);
#
# insert into items(name,price)
# values('none',0),('Computer',3000),('Pen', 15), ('Leptop', 5000) ('Disk',450), ('Printer', 850),;
#
# create table orders (
# order_id serial primary key,
# item1 integer not null,
# foreign key (item1) references items(item_id) on delete restrict,
# item2 integer default 1,
# foreign key (item2) references items(item_id) on delete restrict,
# item3 integer default 1,
# foreign key (item3) references items(item_id) on delete restrict);
#
# insert into orders(item1)
# values (1);
# insert into orders(item1,item2,item3)
# values((select item_id from items where name = 'Computer'),
# (select item_id from items where name = 'Pen'),
# (select item_id from items where name = 'Leptop')),
# ((select item_id from items where name = 'Disk'),
# (select item_id from items where name = 'Computer'),
# (select item_id from items where name = 'Printer'));
# insert into orders(item1,item2)
# values((select item_id from items where name = 'Computer'),
# (select item_id from items where name = 'Leptop'));
#
#
# # -- Create a function that returns the total price for a given order.
#
# create function total_price_order(ord int) returns int as $total_price$
# declare
# 	price1 int;
# 	price2 int;
# 	price3 int;
# begin
# 	price1 = (select price from items join orders on orders.item1 = items.item_id where order_id = ord);
# 	price2 = (select price from items join orders on orders.item2 = items.item_id where order_id = ord);
# 	price3 = (select price from items join orders on orders.item3 = items.item_id where order_id = ord);
# 	return price1+price2+price3;

#
# select * from total_price_order(2);
#
#
