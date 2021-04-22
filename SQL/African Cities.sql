select c2.name
from country as c1
join city as c2
on c1.code = c2.countrycode
where c1.continent = "Africa";
