USE [GaiaMusic]

SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE sp_AddNewInstrument
	@inInstrumentType VARCHAR(50)
	, @inTitle VARCHAR(50)
	, @inDetail VARCHAR(50)
	, @inPrice MONEY 
	, @inGuaranteeBegin DATE
	, @inGuaranteeEnd DATE
	, @inAmount INT
	, @OutResultCode INT OUTPUT

AS
BEGIN
		SET NOCOUNT ON;
		BEGIN TRY
			SELECT 
				@OutResultCode=0 ;

			IF NOT EXISTS (SELECT * FROM dbo.Instruments AS I WHERE I.Title = @inTitle)
				BEGIN

				DECLARE @IdInstrument INT = (SELECT IT.Id FROM dbo.InstrumentTypes AS IT WHERE IT.InstrumentType = @inInstrumentType);

					BEGIN TRANSACTION

						INSERT INTO dbo.Instruments(
							IdInstrumentType,
							Title,
							Detail,
							Price,
							GuaranteeBegin,
							GuaranteeEnd,
							Enabled
							)	

							VALUES(
								@inInstrumentType,
								@inTitle,
								@inDetail,
								@inPrice,
								@inGuaranteeBegin,
								@inGuaranteeEnd,
								1
							)

						UPDATE dbo.Stock
							SET Amount = (SELECT S.Amount FROM dbo.Stock AS S WHERE S.IdInstrument = @IdInstrument) + @inAmount
							WHERE dbo.Stock.IdInstrument = @IdInstrument;

					COMMIT TRANSACTION TSaveMov
				END

			ELSE
				SELECT
					@OutResultCode = 1 ;

			SELECT @OutResultCode;

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
EXECUTE sp_AddNewInstrument 1 , 20 , 0
DROP PROCEDURE sp_AddNewInstrument
*/