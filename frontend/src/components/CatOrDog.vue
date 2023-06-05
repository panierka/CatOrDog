<template>
    <div>
        <TestFetcher/>
        <FileUploader @get-classification="onClassification"/>
        <p v-if="classificationResult !== null">
            Twoje zwierzę to {{ classificationResult }}
        </p>
        <p v-else>
            ???
        </p>
    </div>
</template>

<script lang="ts">
import TestFetcher from './TestFetcher.vue';
import FileUploader from './FileUploader.vue';
import { Component, Vue } from 'vue-facing-decorator';

@Component({
    components: {
        TestFetcher,
        FileUploader
    }
})
export default class CatOrDog extends Vue {
    classificationResult: string | null = null;    

    onClassification(cls: string | null){
        if (cls === null){
            this.classificationResult = null;
            return;
        }

        const outputsMap: { [id: string] : string; } = {
            'cat': 'kot',
            'dog': 'pies'
        }

        this.classificationResult = outputsMap[cls];
    }
}
</script>