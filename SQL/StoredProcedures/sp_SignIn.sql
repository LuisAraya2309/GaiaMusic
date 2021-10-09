USE [GaiaMusic]

SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE sp_SignIn
	@inUsername varchar(50)
    , @inPassword varchar(50)
	, @OutResultCode INT OUTPUT

AS
BEGIN
	BEGIN TRY
	
		IF EXISTS (SELECT * FROM dbo.Users AS U WHERE U.Username = @inUsername) AND
			@inPassword = (SELECT U.Keyword FROM dbo.Users AS U WHERE U.Username = @inUsername) 
			BEGIN
				SELECT 
					@OutResultCode = 0
				
			END

		ELSE 
			BEGIN
				SELECT 
					@OutResultCode = 1
				
			END

		SELECT @OutResultCode AS OutResultCode , (SELECT U.IdUserType FROM dbo.Users AS U WHERE U.Username = @inUsername) AS UserType;

	END TRY
	BEGIN CATCH


			INSERT INTO dbo.Errors	VALUES (
				SUSER_SNAME(),
				ERROR_NUMBER(),
				ERROR_STATE(),
				ERROR_SEVERITY(),
				ERROR_LINE(),
				ERROR_PROCEDURE(),
				ERROR_MESSAGE(),
				GETDATE()
			);

			Set @OutResultCode=50005;
				
	END CATCH;

END
GO

/*
EXECUTE sp_SignIn 'Jorgito' , 'Macroi' , 0
DROP PROCEDURE sp_SignIn
*/
