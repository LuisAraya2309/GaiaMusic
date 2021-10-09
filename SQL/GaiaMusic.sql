USE [master]
GO
/****** Object:  Database [GaiaMusic]    Script Date: 09/10/2021 10:10:47 ******/
CREATE DATABASE [GaiaMusic]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'GaiaMusic', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\GaiaMusic.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'GaiaMusic_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\GaiaMusic_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [GaiaMusic] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [GaiaMusic].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [GaiaMusic] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [GaiaMusic] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [GaiaMusic] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [GaiaMusic] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [GaiaMusic] SET ARITHABORT OFF 
GO
ALTER DATABASE [GaiaMusic] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [GaiaMusic] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [GaiaMusic] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [GaiaMusic] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [GaiaMusic] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [GaiaMusic] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [GaiaMusic] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [GaiaMusic] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [GaiaMusic] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [GaiaMusic] SET  DISABLE_BROKER 
GO
ALTER DATABASE [GaiaMusic] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [GaiaMusic] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [GaiaMusic] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [GaiaMusic] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [GaiaMusic] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [GaiaMusic] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [GaiaMusic] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [GaiaMusic] SET RECOVERY FULL 
GO
ALTER DATABASE [GaiaMusic] SET  MULTI_USER 
GO
ALTER DATABASE [GaiaMusic] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [GaiaMusic] SET DB_CHAINING OFF 
GO
ALTER DATABASE [GaiaMusic] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [GaiaMusic] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [GaiaMusic] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [GaiaMusic] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'GaiaMusic', N'ON'
GO
ALTER DATABASE [GaiaMusic] SET QUERY_STORE = OFF
GO
USE [GaiaMusic]
GO
/****** Object:  Table [dbo].[Errors]    Script Date: 09/10/2021 10:10:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Errors](
	[SUSER_SNAME] [varchar](max) NULL,
	[ERROR_NUMER] [int] NULL,
	[ERROR_STATE] [int] NULL,
	[ERROR_SEVERITY] [int] NULL,
	[ERROR_LINE] [int] NULL,
	[ERROR_PROCEDURE] [varchar](max) NULL,
	[ERROR_MESSAGE] [varchar](max) NULL,
	[GETDATE] [datetime] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Instruments]    Script Date: 09/10/2021 10:10:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Instruments](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[IdInstrumentType] [int] NOT NULL,
	[Title] [varchar](50) NOT NULL,
	[Detail] [text] NOT NULL,
	[Price] [money] NOT NULL,
	[GuaranteeBegin] [date] NOT NULL,
	[GuaranteeEnd] [date] NOT NULL,
	[Enabled] [bit] NOT NULL,
 CONSTRAINT [PK_Instruments] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[InstrumentTypes]    Script Date: 09/10/2021 10:10:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[InstrumentTypes](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[InstrumentType] [varchar](50) NOT NULL,
 CONSTRAINT [PK_InstrumentTypes] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Stock]    Script Date: 09/10/2021 10:10:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Stock](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[IdInstrument] [int] NOT NULL,
	[Amount] [int] NOT NULL,
 CONSTRAINT [PK_Stock] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Transactions]    Script Date: 09/10/2021 10:10:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Transactions](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[IdTransactionType] [int] NOT NULL,
	[IdUser] [int] NOT NULL,
	[IdInstrument] [int] NOT NULL,
	[Amount] [int] NOT NULL,
	[TotalPrice] [money] NOT NULL,
	[TransactionDate] [date] NOT NULL,
 CONSTRAINT [PK_Transactions] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TransactionTypes]    Script Date: 09/10/2021 10:10:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TransactionTypes](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[TransactionType] [varchar](50) NOT NULL,
 CONSTRAINT [PK_TransactionTypes] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Users]    Script Date: 09/10/2021 10:10:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Users](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Firstname] [varchar](50) NOT NULL,
	[Lastname] [varchar](50) NOT NULL,
	[IdUserType] [int] NOT NULL,
	[Username] [varchar](50) NOT NULL,
	[Keyword] [varchar](50) NOT NULL,
	[Enabled] [bit] NOT NULL,
 CONSTRAINT [PK_Users] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[UserTypes]    Script Date: 09/10/2021 10:10:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[UserTypes](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[UserType] [varchar](50) NOT NULL,
 CONSTRAINT [PK_UserTypes] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Instruments]  WITH CHECK ADD  CONSTRAINT [FK_Instruments_InstrumentTypes] FOREIGN KEY([IdInstrumentType])
REFERENCES [dbo].[InstrumentTypes] ([Id])
GO
ALTER TABLE [dbo].[Instruments] CHECK CONSTRAINT [FK_Instruments_InstrumentTypes]
GO
ALTER TABLE [dbo].[Stock]  WITH CHECK ADD  CONSTRAINT [FK_Stock_Instruments] FOREIGN KEY([IdInstrument])
REFERENCES [dbo].[Instruments] ([Id])
GO
ALTER TABLE [dbo].[Stock] CHECK CONSTRAINT [FK_Stock_Instruments]
GO
ALTER TABLE [dbo].[Transactions]  WITH CHECK ADD  CONSTRAINT [FK_Transactions_Instruments] FOREIGN KEY([IdInstrument])
REFERENCES [dbo].[Instruments] ([Id])
GO
ALTER TABLE [dbo].[Transactions] CHECK CONSTRAINT [FK_Transactions_Instruments]
GO
ALTER TABLE [dbo].[Transactions]  WITH CHECK ADD  CONSTRAINT [FK_Transactions_TransactionTypes] FOREIGN KEY([IdTransactionType])
REFERENCES [dbo].[TransactionTypes] ([Id])
GO
ALTER TABLE [dbo].[Transactions] CHECK CONSTRAINT [FK_Transactions_TransactionTypes]
GO
ALTER TABLE [dbo].[Transactions]  WITH CHECK ADD  CONSTRAINT [FK_Transactions_Users] FOREIGN KEY([IdUser])
REFERENCES [dbo].[Users] ([Id])
GO
ALTER TABLE [dbo].[Transactions] CHECK CONSTRAINT [FK_Transactions_Users]
GO
ALTER TABLE [dbo].[Users]  WITH CHECK ADD  CONSTRAINT [FK_Users_UserTypes] FOREIGN KEY([IdUserType])
REFERENCES [dbo].[UserTypes] ([Id])
GO
ALTER TABLE [dbo].[Users] CHECK CONSTRAINT [FK_Users_UserTypes]
GO
/****** Object:  StoredProcedure [dbo].[sp_AddInstrument]    Script Date: 09/10/2021 10:10:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[sp_AddInstrument]
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
/****** Object:  StoredProcedure [dbo].[sp_AddNewInstrument]    Script Date: 09/10/2021 10:10:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[sp_AddNewInstrument]
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
/****** Object:  StoredProcedure [dbo].[sp_SignIn]    Script Date: 09/10/2021 10:10:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[sp_SignIn]
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
/****** Object:  StoredProcedure [dbo].[sp_SignUp]    Script Date: 09/10/2021 10:10:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[sp_SignUp]
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
/****** Object:  StoredProcedure [dbo].[sp_SuspendAccount]    Script Date: 09/10/2021 10:10:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[sp_SuspendAccount]
	@inUsername varchar(50)
    , @inPassword varchar(50)
	, @OutResultCode INT OUTPUT

AS
BEGIN
		SET NOCOUNT ON;
		BEGIN TRY
			SELECT @OutResultCode=0 ;

			IF EXISTS (SELECT * FROM dbo.Users AS U WHERE U.Username = @inUsername) AND
				@inPassword = (SELECT U.Keyword FROM dbo.Users AS U WHERE U.Username = @inUsername) 

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
/****** Object:  StoredProcedure [dbo].[sp_SuspendAccountAdmin]    Script Date: 09/10/2021 10:10:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[sp_SuspendAccountAdmin]
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
USE [master]
GO
ALTER DATABASE [GaiaMusic] SET  READ_WRITE 
GO
