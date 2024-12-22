CREATE TABLE [dbo].[DataPipel_Demo] (
    [left_BikepointID]     NVARCHAR (MAX) NULL,
    [left_Street]          NVARCHAR (MAX) NULL,
    [left_Neighbourhood]   NVARCHAR (MAX) NULL,
    [left_Latitude]        FLOAT (53)     NULL,
    [left_Longitude]       FLOAT (53)     NULL,
    [left_No_Bikes]        BIGINT         NULL,
    [left_No_Empty_Docks]  BIGINT         NULL,
    [right_BikepointID]    NVARCHAR (MAX) NULL,
    [right_Street]         NVARCHAR (MAX) NULL,
    [right_Neighbourhood]  NVARCHAR (MAX) NULL,
    [right_Latitude]       FLOAT (53)     NULL,
    [right_Longitude]      FLOAT (53)     NULL,
    [right_No_Bikes]       BIGINT         NULL,
    [right_No_Empty_Docks] BIGINT         NULL
);


GO

