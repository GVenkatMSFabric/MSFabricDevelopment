
CREATE PROCEDURE GetCityName
(
@CityName VARCHAR(100)
)
AS
BEGIN
  SET NOCOUNT ON;
  SELECT * FROM Employee WHERE EmpLocation = @CityName
END

GO

