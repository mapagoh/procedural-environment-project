create table crosslinkage
(
    ID int null,
    speciescode varchar(10),
    speciesname varchar(155),
    sub_unit varchar(255),
    assessment_code_EU int,
    assessment_specname_EU varchar(255),
    season int,
    assessment_code_trend_breeding int,
    assessment_specname_trend_breeding varchar(155),
    assessment_code_trend_wintering int,
    assessment_specname_trend_wintering varchar(155),
    addtionnal_record int

)

BULK INSERT crosslinkage FROM "../../data/crosslinkage_table.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table bgmeasures
(
    bgreporthash varchar(60),
    sitecode varchar(30),
    sitename varchar(300),
    project_year int,
    project_title varchar(255),
    impact varchar(255)

)

BULK INSERT bgmeasures FROM "../../data/data_bgmeasures.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table bgmonitoring
(
    bgreporthash varchar(60),
    monitoring_title varchar(255),
    monitoring_year int,
    monitoring_reference varchar(255)
)

BULK INSERT bgmonitoring FROM "../../data/data_bgmonitoring.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table bgnon_native_bird
(
    bgreporthash varchar(60),
    speciesname varchar(10),
    subspecies_name varchar(30),
    introduction varchar(60),
    consultation_date varchar(30)
)

BULK INSERT bgnon_native_bird FROM "../../data/data_bgnon_native_bird.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table bgpublication
(
    bgreporthash varchar(60),
    other_publication_title varchar(255),
    other_publication_year int,
    other_publication_reference varchar(255)

)

BULK INSERT bgpublication FROM "../../data/data_bgpublication.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table birds_check_list
(
    country varchar(10),
    country_isocode varchar(10),
    speciescode varchar(10),
    speciesname varchar(30),
    sub_unit varchar(60),
    euringcode int,
    annexI varchar(10),
    season varchar(10),
    population_size_unit varchar(30),
    spa_trigger int,
    non_native int,
    presence int,
    assessment_code_EU int,
    assessment_specname_EU varchar(60),
    assessment_code_trend int,
    assessment_specname_trend varchar(155)
) 

BULK INSERT birds_check_list FROM "../../data/data_birds_check_list.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table birds_eu_breeding_trends
(
    assessment_code_trend int,
    assessment_specname_trend varchar(155),
    population_size_unit varchar(30),
    BrPopSizeMin int,
    BrPopSizeMax int,
    BrPopSizeMinRnd int,
    BrPopSizeMaxRnd int,
    BrPopTrdSht varchar(10),
    BrPopTrdLng varchar(10),
    BrRngSize float,
    BrRngSizeRnd int,
    BrRngTrdSht varchar(10),
    BrRngTrdLng varchar(10)
)

BULK INSERT birds_eu_breeding_trends FROM "../../data/data_birds_eu_breeding_trends.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table birds_eu_status
(
    assessment_code_EU int,
    assessment_specname_EU varchar(155),
    season varchar(10),
    Population_status varchar(30),
    population_size_unit varchar(30),
    PopSizeMin int,
    PopSizeMax int,
    PopSizeMinRnd int,
    PopSizeMaxRnd int,
    PopTrdSht varchar(10),
    PopTrdLng varchar(10),
    Contribution_target1 varchar(30),
    addtionnal_record int
)

BULK INSERT birds_eu_status FROM "../../data/data_birds_eu_status.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table birds_eu_wintering_trends
(
    assessment_code_trend int,
    assessment_specname_trend varchar(155),
    population_size_unit varchar(60),
    WiPopSizeMin int,
    WiPopSizeMax int,
    WiPopSizeMinRnd int,
    WiPopSizeMaxRnd int,
    WiPopTrdSht varchar(10),
    WiPopTrdLng varchar(10),
)

BULK INSERT birds_eu_wintering_trends FROM "../../data/data_birds_eu_wintering_trends.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table bmeadures
(
  measurehash varchar(60),
  specieshash varchar(60),
  measurecode float,
  type_legal int,
  type_administrative int,
  type_contractual int,
  type_recurrent int,
  type_oneoff int,
  rankingcode varchar(10),
  location_inside int,
  location_outside int,
  location_both int,
  broad_evaluation_maintain int,
  broad_evaluation_enhance int,
  broad_evaluation_longterm int,
  broad_evaluation_noeffect int,
  broad_evaluation_unknown int,
  broad_evaluation_notevaluated int,
)

BULK INSERT bmeasures FROM "../../data/data_bmeasures.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table bpressures_threats
(
    pressurethreathash varchar(60),
    specieshash varchar(60),
    pressurecode varchar(30),
    rankingcode varchar(10),
    quality int,
    location int,
    sources varchar(255)
)

BULK INSERT bpressures_threats FROM "../../data/data_bpressures_threats.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);

create table species_birds_maes_EU27
(
    speciesname varchar(30),
    sub_unit varchar(30),
    speciescode varchar(10),
    euringcode int,
    codeeco varchar(30),
    typeasso varchar(10),
    season varchar(10),
    region varchar(10),
)

BULK INSERT species_birds_maes_EU27 FROM "../../data/species_birds_maes_EU27.csv"
WITH(FIRSTROW = 2, FIELDTERMINATOR = ",", ROWTERMINATOR = "\n", BATCHSIZE = 25000, MAXERRORS = 8);


