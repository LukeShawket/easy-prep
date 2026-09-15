import pandas as pd
from pathlib import Path

class Exporter:


    def export(df, export_schema):
        export_format = export_schema["format"].lower()
        include_header = export_schema["include_header"]
        include_index = export_schema["include_index"]
        folder_path = Path(export_schema["folder_path"])

        folder_path.mkdir(parents=True, exist_ok=True)


        file_path = folder_path / f"export.{export_format}"

        if export_format == "xlsx":
            df.to_excel(file_path, header=include_header, index=include_index)

        elif export_format == "csv":
            df.to_csv(file_path, header=include_header, index=include_index)

        elif export_format == "txt":
            df.to_csv(
                file_path,
                sep="\t",
                header=include_header,
                index=include_index
            )

        elif export_format == "json":
            df.to_json(file_path, orient="records", indent=4)

        else:
            raise ValueError(f"Unsupported format: {export_format}")

        return "Exported!"