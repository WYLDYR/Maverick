def install(id,path):
    from src.data.dataRunner import getUserData
    from src.prompt.inputCases import ProgramID

    data = getUserData()

    data["programs"].append(
        ProgramID(
            id,
            path
        )
    )

    data.close()