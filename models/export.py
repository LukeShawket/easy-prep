import pandas as pd
from pathlib import Path

class Exporter:

    @staticmethod
    def export(df, export_schema):
        file_name = export_schema["file_name"]
        export_format = export_schema["format"].lower()
        include_header = export_schema["include_header"]
        include_index = export_schema["include_index"]
        folder_path = Path(export_schema["folder_path"])

        folder_path.mkdir(parents=True, exist_ok=True)


        file_path = folder_path / f"{file_name}.{export_format}"

        if export_format == "xlsx":
            df.to_excel(file_path, header=include_header, index=include_index)

        elif export_format == "csv":
            df.to_csv(file_path, header=include_header, index=include_index)

        elif export_format == "txt":
            if include_header:
                lines = df.to_string(header=include_header, index=include_index)
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(lines)
            else:
                lines = []
                
                for _, row in df.iterrows():
                    lines.append("".join(map(str, row.fillna(""))))

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(lines))

        elif export_format == "json":
            df.to_json(file_path, orient="records", indent=4)

        else:
            raise ValueError(f"Unsupported format: {export_format}")

        return "Exported!"