select*from titanic;
SELECT Name, Age FROM titanic WHERE Age > 30;
SELECT name, Pclass FROM titanic WHERE sex = 'female' or Pclass = 1;
SELECT name, age, Survived FROM titanic WHERE survived = 1 ORDER BY Age;
SELECT name from titanic WHERE SibSp=0 and Parch=0;
SELECT name, Pclass FROM titanic WHERE Fare>100;
SELECT name, Pclass, age FROM titanic WHERE Pclass !=1 and age>18;
SELECT*FROM titanic WHERE Survived=0 and SibSp=0 and Parch=0;
SELECT name, Fare, Pclass FROM titanic WHERE Pclass<10 and Pclass !=3