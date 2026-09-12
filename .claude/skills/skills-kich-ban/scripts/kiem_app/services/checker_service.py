import re
from kiem_app.models.script_data import ScriptData
from kiem_app.core.logger import Logger

class CheckerService:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.cliches = ["little did she know", "tears streamed down her face", "suddenly", "out of nowhere"]
        self.eval_adjectives = ["incredible", "devastating", "heartbreaking", "shocking"]

    def check_all(self, script_data: ScriptData):
        self._check_length(script_data)
        self._check_title(script_data)
        self._check_sentences(script_data)
        self._check_numbers(script_data)
        self._check_cliches_adjectives(script_data)
        self._check_dialogue_ratio(script_data)
        self._check_youtube_desc(script_data)

    def _count_words(self, text: str) -> int:
        return len(re.findall(r'\b\w+\b', text))

    def _check_length(self, script_data: ScriptData):
        total_words = self._count_words(script_data.raw_content)
        hook_words = self._count_words(script_data.hook)
        
        if 7300 <= total_words <= 8050:
            self.logger.success(f"THAN.do-dai: {total_words} words (7300-8050)")
        else:
            self.logger.fail(f"THAN.do-dai: {total_words} words (expected 7300-8050)")
            
        if 115 <= hook_words <= 175:
            self.logger.success(f"HOOK.do-dai: {hook_words} words (115-175)")
        else:
            self.logger.fail(f"HOOK.do-dai: {hook_words} words (expected 115-175)")

    def _check_title(self, script_data: ScriptData):
        title = script_data.title
        if not title:
            self.logger.fail("TITLE: No title found")
            return
            
        chars = len(title)
        dash_count = title.count('—')
        has_black = 'black' in title.lower()
        clauses = len(re.split(r'[,;]|\s+and\s+', title))
        
        if 90 <= chars <= 100:
            self.logger.success(f"TITLE.tran chars: {chars} (90-100)")
        else:
            self.logger.fail(f"TITLE.tran chars: {chars} (expected 90-100)")
            
        if dash_count == 1:
            self.logger.success("TITLE.tran dash: exactly 1 '—'")
        else:
            self.logger.fail(f"TITLE.tran dash: {dash_count} '—' found (expected 1)")
            
        if has_black:
            self.logger.success("TITLE.tran 'Black': Present")
        else:
            self.logger.fail("TITLE.tran 'Black': Missing")
            
        if clauses <= 2:
            self.logger.success(f"TITLE.tran clauses: {clauses} (<= 2)")
        else:
            self.logger.fail(f"TITLE.tran clauses: {clauses} (expected <= 2)")

    def _check_sentences(self, script_data: ScriptData):
        # A simple approximation for sentence splitting
        sentences = re.split(r'[.!?]\s+', script_data.body)
        sentences = [s for s in sentences if s.strip()]
        if not sentences:
            return
            
        lengths = [self._count_words(s) for s in sentences]
        long_sentences = sum(1 for l in lengths if l > 40)
        short_sentences = sum(1 for l in lengths if l <= 6)
        
        if long_sentences <= 2:
            self.logger.success(f"VAN.nhip-cau: {long_sentences} sentences > 40 words")
        else:
            self.logger.fail(f"VAN.nhip-cau: {long_sentences} sentences > 40 words (max 2)")

    def _check_numbers(self, script_data: ScriptData):
        # Simply check for digits in hook/body
        digits = re.findall(r'\b\d+\b', script_data.hook + " " + script_data.body)
        if digits:
            self.logger.fail(f"6-giong-van: Arabic numerals found: {set(digits)}")
        else:
            self.logger.success("6-giong-van: No Arabic numerals in hook/body")

    def _check_cliches_adjectives(self, script_data: ScriptData):
        content_lower = script_data.raw_content.lower()
        found = []
        for word in self.cliches + self.eval_adjectives:
            if word in content_lower:
                found.append(word)
        if found:
            self.logger.fail(f"6-giong-van: Cliches/eval adjectives found: {found}")
        else:
            self.logger.success("6-giong-van: No cliches/eval adjectives found")

    def _check_dialogue_ratio(self, script_data: ScriptData):
        dialogues = re.findall(r'"([^"]*)"', script_data.raw_content)
        dialogue_words = sum(self._count_words(d) for d in dialogues)
        total = self._count_words(script_data.raw_content)
        if total > 0:
            ratio = dialogue_words / total
            self.logger.success(f"VAN.ngoi-ke dialogue ratio: {ratio:.1%}")

    def _check_youtube_desc(self, script_data: ScriptData):
        desc = script_data._extract_section("## 9 — Mô tả YouTube")
        if not desc:
            return
            
        chars = len(desc.strip())
        checkmarks = desc.count("✔️")
        hashtags = len(re.findall(r'#\w+', desc))

        if 1400 <= chars <= 1500:
            self.logger.success(f"9-mo-ta-youtube chars: {chars} (1400-1500)")
        else:
            self.logger.fail(f"9-mo-ta-youtube chars: {chars} (expected 1400-1500)")
            
        if checkmarks >= 3:
            self.logger.success(f"9-mo-ta-youtube checkmarks: {checkmarks}")
        else:
            self.logger.fail(f"9-mo-ta-youtube checkmarks: {checkmarks} (expected >= 3)")
            
        if 8 <= hashtags <= 10:
            self.logger.success(f"9-mo-ta-youtube hashtags: {hashtags} (8-10)")
        else:
            self.logger.fail(f"9-mo-ta-youtube hashtags: {hashtags} (expected 8-10)")
