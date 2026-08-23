DECLARE @UpperLimit INT, @LowerLimit INT

SET @UpperLimit = 500
SET @LowerLimit = 100

DECLARE @N INT, @P INT
DECLARE @Numbers TABLE (Number INT NULL)
DECLARE @Composite TABLE (Number INT NULL)

SET @P = @UpperLimit

IF (@LowerLimit > @UpperLimit OR @UpperLimit < 0 OR @LowerLimit < 0 )
	BEGIN
		PRINT 'Incorrect Range'
	END	
ELSE
	BEGIN
		WHILE @P > @LowerLimit
			BEGIN
				INSERT INTO @Numbers(Number) VALUES (@P)
				SET @N = 2
				WHILE @N <= @UpperLimit/2
					BEGIN
						IF ((@P%@N = 0 AND @P <> @N) OR (@P IN (0, 1)))
							BEGIN
								INSERT INTO @Composite(Number) VALUES (@P)
								BREAK
							END
						SET @N = @N + 1
					END
				SET @P = @P - 1
			END
		SELECT Number FROM @Numbers
		WHERE Number NOT IN (SELECT Number FROM @Composite)
		ORDER BY Number
		END
