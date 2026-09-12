class ScriptData:
    def __init__(self, raw_content: str):
        self.raw_content = raw_content
        # Extract title, hook, body, youtube desc if any
        self.title = self._extract_title()
        self.hook = self._extract_section("## Hook")
        self.body = self._extract_section("## Thân")
        
    def _extract_title(self) -> str:
        for line in self.raw_content.splitlines():
            if line.startswith("# "):
                return line[2:].strip()
        return ""

    def _extract_section(self, header_prefix: str) -> str:
        lines = self.raw_content.splitlines()
        in_section = False
        section_lines = []
        for line in lines:
            if line.startswith(header_prefix):
                in_section = True
                continue
            if in_section and line.startswith("## "):
                break
            if in_section:
                section_lines.append(line)
        return "\n".join(section_lines).strip()
