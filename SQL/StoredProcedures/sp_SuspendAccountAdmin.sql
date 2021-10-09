USE [GaiaMusic]

SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE sp_SuspendAccountAdmin
	@inUsername varchar(50)
	, @OutResultCode INT OUTPUT

AS
BEGIN
		SET NOCOUNT ON;
		BEGIN TRY
			SELECT @OutResultCode=0 ;

			IF EXISTS (SELECT * FROM dbo.Users AS U WHERE U.Username = @inUsername) 	 

				BEGIN
					BEGIN TRANSACTION 
						UPDATE dbo.Users
							SET Enabled = 0
							WHERE Users.Username = @inUsername

					COMMIT TRANSACTION TSaveMov
				END

				ELSE 
					BEGIN
						SELECT @OutResultCode = 1
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
EXECUTE sp_SuspendAccountAdmin 'Jorgito' , 0
DROP PROCEDURE sp_SuspendAccountAdmin
SELECT * FROM dbo.Users
*/