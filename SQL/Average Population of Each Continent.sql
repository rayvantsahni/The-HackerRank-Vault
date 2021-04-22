select c2.continent, floor(avg(c1.population))
from city as c1
join country as c2
on c1.countrycode = c2.code
group by c2.continent;
