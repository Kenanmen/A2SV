class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        lett = []

        for log in logs:
            identifier, content = log.split(" ", 1)

            if content[0].isdigit():
                digits.append(log)
            else:
                lett.append((content, identifier, log))

        lett.sort(key=lambda x: (x[0], x[1]))

        sorted_lett = [log[2] for log in lett]

        return sorted_lett + digits