USE [GaiaMusic]

SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE sp_AddInstrument
	@inIdInstrument INT
	, @inAmount INT
	, @OutResultCode INT OUTPUT

AS
BEGIN
		SET NOCOUNT ON;
		BEGIN TRY
			SELECT 
				@OutResultCode=0 ;

			BEGIN TRANSACTION

				UPDATE dbo.Stock
					SET Amount = (SELECT S.Amount FROM dbo.Stock AS S WHERE S.IdInstrument = @inIdInstrument) + @inAmount
					WHERE dbo.Stock.IdInstrument = @inIdInstrument;

			COMMIT TRANSACTION TSaveMov
			

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
EXECUTE sp_AddInstrument 1 , 20 , 0
DROP PROCEDURE sp_AddInstrument
*/