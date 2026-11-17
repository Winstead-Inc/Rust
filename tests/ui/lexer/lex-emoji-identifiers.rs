fn invalid_emoji_usages()
{
    let arrow ↔ ️ = "basic emoji";
    //~ ERROR: identifiers cannot contain emoji
    let planet 🪐 = "basic emoji";
    //~ ERROR: identifiers cannot contain emoji
    let wireless 🛜 = "basic emoji";
    //~ ERROR: identifiers cannot contain emoji
    // FIXME
    let key1 ️ ⃣ = "keycap sequence";
    //~ ERROR: unknown start of token
    //~^ WARN: identifier contains an uncommon character: '\u{fe0f}'
    let flag 🇺 🇳 = "flag sequence";
    //~ ERROR: identifiers cannot contain emoji
    let wales 🏴 = "tag sequence";
    //~ ERROR: identifiers cannot contain emoji
    let folded 🙏 🏿 = "modifier sequence";
    //~ ERROR: identifiers cannot contain emoji
}

fn main() { invalid_emoji_usages(); }
