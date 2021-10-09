USE [GaiaMusic]

SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE sp_SignUp
	@inFirstname varchar(50)
	, @inLastname varchar(50)
	, @inUsername varchar(50)
    , @inPassword varchar(50)
	, @inUserType varchar(50)
	, @OutResultCode INT OUTPUT

AS
BEGIN
		SET NOCOUNT ON;
		BEGIN TRY
			SELECT
				@OutResultCode=0 ;

			IF NOT EXISTS (SELECT * FROM dbo.Users AS U WHERE U.Username = @inUsername)
				BEGIN
					
					BEGIN TRANSACTION TSaveMov
						INSERT INTO dbo.Users
							(
								Firstname,
								Lastname,
								IdUserType,
								Username,
								Keyword,
								Enabled
				
							)
							VALUES
							(
								@inFirstname,
								@inLastname,
								(SELECT UT.Id FROM dbo.UserTypes AS UT WHERE UT.UserType = @inUserType),
								@inUsername,
								@inPassword,
								1
							)
					COMMIT TRANSACTION TSaveMov;
				END
			ELSE
				BEGIN
					SELECT
						@OutResultCode = 1 ;
				END

			SELECT @OutResultCode AS OutResultCode;

		END TRY
		BEGIN CATCH

				IF @@Trancount>0 
					ROLLBACK TRANSACTION TSaveMov;

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

		SET NOCOUNT OFF;

END
GO

/*
EXECUTE sp_SignUp 'Jorge','Bonilla','Jorgito' , 'Macroi' , 'Customer' , 0
DROP PROCEDURE sp_SignUp
SELECT * FROM dbo.Users
*/
