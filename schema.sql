create table if exists ALL;

create table `databases` (
  `id` int not null auto_increment,
  `name` varchar(80) default null,
  primary key (`id`)
);