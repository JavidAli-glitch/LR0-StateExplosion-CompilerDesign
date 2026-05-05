import pandas as pd

lr0_states = {
    "I0": ["S' -> .S", "S -> .CC", "C -> .cC", "C -> .d"],
    "I1": ["S' -> S."],
    "I2": ["S -> C.C", "C -> .cC", "C -> .d"],
    "I3": ["C -> c.C", "C -> .cC", "C -> .d"],
    "I4": ["C -> d."],
    "I5": ["S -> CC."],
    "I6": ["C -> cC."],
    "I7": ["C -> c.C", "C -> .cC", "C -> .d"],
    "I8": ["C -> d."],
    "I9": ["C -> cC."],
}

data = []
for state, items in lr0_states.items():
    data.append({"State": state, "Item_Count": len(items)})

df = pd.DataFrame(data)

total_states = len(df)
total_items  = df["Item_Count"].sum()
avg_items    = round(total_items / total_states, 2)
THRESHOLD    = 2.5

df["Average_Items_Per_State"] = avg_items
df["Is_State_Explosion"]      = df["Average_Items_Per_State"] > THRESHOLD

print("=" * 65)
print("    LR(0) STATE EXPLOSION DETECTION REPORT")
print("=" * 65)
print(df[["State","Item_Count","Average_Items_Per_State","Is_State_Explosion"]].to_string(index=False))
print(f"\nTotal States            : {total_states}")
print(f"Total Items             : {total_items}")
print(f"Average Items Per State : {avg_items}")
print(f"Threshold               : {THRESHOLD}")
print(f"Is_State_Explosion      : {avg_items > THRESHOLD}")
if avg_items > THRESHOLD:
    print("WARNING: STATE EXPLOSION DETECTED")
else:
    print("OK: No state explosion detected")
print("=" * 65)
