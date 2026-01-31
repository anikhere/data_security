from dataclasses import dataclass
class ArtifactsEntity:
    @dataclass
    class Artifact:
        trained_file_path: str
        test_file_path: str
