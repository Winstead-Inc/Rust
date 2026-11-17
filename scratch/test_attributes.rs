// Short attribute fits on one line -> State 1 Monolith:
#[derive(Clone, Copy, Debug)]
struct Short;

// Long attribute exceeds 160 columns:
#[derive(Clone, Copy, Debug, PartialEq, Eq, PartialOrd, Ord, Hash, Default, Serialize, Deserialize, Subcommand, Parser, ValueEnum, Archive, RkyvSerialize, RkyvDeserialize)]
struct Long;
