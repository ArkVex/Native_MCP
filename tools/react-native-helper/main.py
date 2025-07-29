def generate_component(params):
    name = params.get("component_name", "MyComponent")
    code = f"""import React from 'react';\nimport {{ View, Text }} from 'react-native';\n\nconst {name} = () => (\n  <View>\n    <Text>{name} works!</Text>\n  </View>\n);\n\nexport default {name};\n"""
    return {"component": code} 