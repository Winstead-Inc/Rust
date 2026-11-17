use std::collections::HashMap;

pub fn update_map(map: &mut HashMap<String, usize>, key: String, val: usize)
{
    if !map.contains_key(&key)
    {
        map.insert(key, val);
    }
    else
    {
        map.insert(key, val + 1);
    }
}
